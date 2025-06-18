import React from "react";
import { View, Text, StyleSheet, ActivityIndicator } from "react-native";
import * as FileSystem from "expo-file-system";
import { Asset } from "expo-asset";
import { readString } from "react-native-csv";
import PickerSelect from "./PickerSelect"; // Assuming you have a custom PickerSelect component

const CentroSelector = ({parroquia,municipio, onSelect}) => {
  const [centros, setcentros] = React.useState([]);
  const [selectedCentro, setSelectedCentro] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  
  const parseCSV = (csvText) => {
    try{
        const { data } = readString(csvText, {
            header: true,
            skipEmptyLines: true,
        });
        return data;
    }
    catch (error) {
        console.error("Error parsing CSV:", error);
        return [];
    }
  };

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        
        const asset = Asset.fromModule(require("../assets/centros.csv"));
        console.log(asset.localUri);
        
        if (!asset.localUri) {
          await asset.downloadAsync();
        }
        // crear una ruta valida
        const csvUri = asset.localUri || asset.uri;

        const fileInfo = await FileSystem.getInfoAsync(csvUri);
        
        if (!fileInfo.exists) {
          console.error("File does not exist");
          throw new Error("File does not exist");
          return;
        }

        const destPath = `${FileSystem.cacheDirectory}centros.csv`;
        await FileSystem.copyAsync({
          from: csvUri,
          to: destPath,
        });
        
        const response = await FileSystem.readAsStringAsync(destPath, {
            encoding: FileSystem.EncodingType.UTF8});

        const parsedData = parseCSV(response);
        setcentros(parsedData);
        setLoading(false);
      } catch (error) {
        console.error("Error reading file:", error);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
        <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#0000ff" />
        </View>
    );
  }

    // Filtrar las centros por el municipio seleccionado
    const filteredcentros = centros.filter(c=> c.municipio === municipio && c.parroquia === parroquia).map((centro) => ({
        key: centro.centro,
        label: centro.centro,
        value: centro.centro,
    }));

return (
    
        <PickerSelect
        items={filteredcentros}
        selectedValue={null}
        onValueChange={onSelect}
        placeholder="Seleccione un centro electoral"
        />
);
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: "#fff",
  },
  center: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  item: {
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
  },
  itemText: {
    fontSize: 18,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
    gap: 10,
  },
});

const pickerSelectStyles = StyleSheet.create({
  inputIOS: {
    fontSize: 8,
    paddingVertical: 12,
    paddingHorizontal: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 4,
    color: "black",
    paddingRight: 30, // to ensure the text is never behind the icon
  },
  inputAndroid: {
    paddingVertical: 8,
    paddingHorizontal: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 4,
    color: "black",
    paddingRight: 30, // to ensure the text is never behind the icon
  },
});

export default CentroSelector;