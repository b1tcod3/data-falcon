import React from "react";
import { View, Text, StyleSheet, ActivityIndicator } from "react-native";
import * as FileSystem from "expo-file-system";
import { Asset } from "expo-asset";
import { readString } from "react-native-csv";
import RNPickerSelect from "react-native-picker-select";
import {appStyles} from "../styles/appStyles";
import {pickerSelectStyles} from "../styles/pickerStyles";

const ParroquiaSelector = ({municipio,onSelect}) => {
  const [parroquias, setParroquias] = React.useState([]);
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
        
        const asset = Asset.fromModule(require("../assets/parroquias.csv"));
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

        const destPath = `${FileSystem.cacheDirectory}parroquias.csv`;
        await FileSystem.copyAsync({
          from: csvUri,
          to: destPath,
        });
        
        const response = await FileSystem.readAsStringAsync(destPath, {
            encoding: FileSystem.EncodingType.UTF8});

        const parsedData = parseCSV(response);
        setParroquias(parsedData);
        setLoading(false);
      } catch (error) {
        console.error("Error reading file:", error);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
        <View style={appStyles.loadingContainer}>
            <ActivityIndicator size="large" color="#0000ff" />
        </View>
    );
  }

    // Filtrar las parroquias por el municipio seleccionado
    const filteredParroquias = parroquias.filter(p=> p.municipio === municipio);

  return (
    <View style={appStyles.container}>
      <RNPickerSelect
        onValueChange={onSelect}
        items={filteredParroquias.map((parroquia) => ({
          key: parroquia.parroquia,
          label: parroquia.parroquia,
          value: parroquia.parroquia,
        }))}
        placeholder={{ label: municipio?"Seleccione un parroquia":"seleccione un municipio", value: null }}
        disabled={!municipio || loading} 
        style={pickerSelectStyles}
        useNativeAndroidPickerStyle={false}
        Icon={()=><View style="{pickerSelectStyle.selectorIcon}"/>}
        />
    </View>
  );
};

export default ParroquiaSelector;