import React from "react";
import { View, Text, StyleSheet, ActivityIndicator } from "react-native";
import * as FileSystem from "expo-file-system";
import { Asset } from "expo-asset";
import { readString } from "react-native-csv";
import RNPickerSelect from "react-native-picker-select";
import {pickerSelectStyles} from "../styles/pickerStyles";
import {appStyles} from "../styles/appStyles";

const MunicipioSelector = ({onSelect}) => {
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

  return (
    <View style={appStyles.container}>
      <RNPickerSelect
        onValueChange={onSelect}
        items={municipios.map((municipio) => ({
          key: municipio.MUNICIPIO,
          label: municipio.MUNICIPIO,
          value: municipio.MUNICIPIO,
        }))}
        placeholder={{ label: "Seleccione un municipio", value: null }}
        style={pickerSelectStyles}
        useNativeAndroidPickerStyle={false}
        Icon={()=><View style="{pickerSelectStyle.selectorIcon}"/>}
        />
    </View>
  );
};


export default MunicipioSelector;