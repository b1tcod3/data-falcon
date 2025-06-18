import React from "react";
import { View, Text, FlatList, StyleSheet, ActivityIndicator } from "react-native";
import * as FileSystem from "expo-file-system";
import { Asset } from "expo-asset";
import { readString } from "react-native-csv";

const MunicipioList = () => {
  const [municipios, setMunicipios] = React.useState([]);
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
        
        const asset = Asset.fromModule(require("../assets/municipios.csv"));
        console.log(asset.localUri);
        
        if (!asset.localUri) {
          await asset.downloadAsync();
        }
        // crear una ruta valida
        const csvUri = asset.localUri || asset.uri;

        const fileInfo = await FileSystem.getInfoAsync(csvUri);
        console.log("File info:", fileInfo);
        if (!fileInfo.exists) {
          console.error("File does not exist");
          throw new Error("File does not exist");
          return;
        }

        const destPath = `${FileSystem.cacheDirectory}municipios.csv`;
        await FileSystem.copyAsync({
          from: csvUri,
          to: destPath,
        });
        
        const response = await FileSystem.readAsStringAsync(destPath, {
            encoding: FileSystem.EncodingType.UTF8});

        const parsedData = parseCSV(response);
        setMunicipios(parsedData);
        setLoading(false);
        console.log("Parsed data:", parsedData);
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

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Municipios</Text>
      <FlatList
        data={municipios}
        keyExtractor={(item) => item.MUNICIPIO}
        renderItem={({ item }) => (
          <View style={styles.item}>
            <Text style={styles.itemText}>{item.MUNICIPIO}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#fff",
  },
  center: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
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
  },
});
export default MunicipioList;