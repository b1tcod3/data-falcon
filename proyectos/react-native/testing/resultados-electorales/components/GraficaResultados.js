import React, { useState, useEffect } from "react";
import { View, Text, StyleSheet, ActivityIndicator, Dimensions } from "react-native";
import * as FileSystem from "expo-file-system";
import { Asset } from "expo-asset";
import { readString } from "react-native-csv";
import { VictoryLine, VictoryChart, VictoryTheme, VictoryLegend, VictoryAxis, VictoryLabel } from "victory-native";
import { theme } from "../theme";

const GraficaResultados = ({municipio,parroquia,centro}) => {

  const [resultados, setResultados] = React.useState([]);
  const [suma, setSuma] = React.useState([]);
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

  useEffect(() => {
    const fetchData = async () => {
      try {
        
        const asset = Asset.fromModule(require("../assets/resultados.csv"));
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

        const destPath = `${FileSystem.cacheDirectory}resultados.csv`;
        await FileSystem.copyAsync({
          from: csvUri,
          to: destPath,
        });
        
        const response = await FileSystem.readAsStringAsync(destPath, {
            encoding: FileSystem.EncodingType.UTF8});

        const parsedData = parseCSV(response);
        setResultados(parsedData);
        console.log(parsedData);
        setLoading(false);
      } catch (error) {
        console.error("Error reading file:", error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const processarSuma = () => {
      let filterResultados = resultados;
      if(municipio){
        filterResultados = filterResultados.filter((resultado) => resultado.MUNICIPIO === municipio);

        if(parroquia){
          filterResultados = filterResultados.filter((resultado) => resultado.PARROQUIA === parroquia);

          if(centro){
            filterResultados = filterResultados.filter((resultado) => resultado.NOMBRE === centro);
          }
        }
      }
      const sumas = filterResultados.reduce((acc, resultado) => {
        const { AN2015, REG2017, PRES2018, REG2021 } = resultado;
        acc['AN2015'] = (acc['AN2015'] || 0) + parseInt(AN2015);
        acc['REG2017'] = (acc['REG2017'] || 0) + parseInt(REG2017);
        acc['PRES2018'] = (acc['PRES2018'] || 0) + parseInt(PRES2018);
        acc['REG2021'] = (acc['REG2021'] || 0) + parseInt(REG2021);
        return acc;
      }, {});

      setSuma(sumas);
      console.log("Suma:", suma);
    };
    processarSuma();
    },[municipio,parroquia,centro,resultados]);  

  if (loading) {
    return (
        <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#0000ff" />
        </View>
    );
  }
    
return (
    <View style={styles.container}>
      <Text style={styles.title}>
        Resultados por Municipio: {municipio} Parroquia: {parroquia} Centro: {centro}
      </Text>
      <VictoryChart
        theme={{...VictoryTheme.clean,
        axis: {
          style:{
            tickLabels: {fill: theme.colors.text},
            axisLabel: {fill: theme.colors.text},
            grid: { stroke: 'transparent'},
            ticks: {
              stroke: "#404040",
              size: 5
            },
            tickLabels:{
              fill: '#888888'
            }
          }
        }
        }}
        width={Dimensions.get("window").width - 40}
        height={300}
        padding={{ top: 40, bottom: 60, left: 50, right: 30 }}
        domainPadding={20}
        >
          <VictoryAxis 
          label="Elección"
          style={{
            axisLabel: { padding: 30 },
            tickLabels: { textAnchor:'end'},
          }}
          />
          
          {
            Object.keys(suma).length > 0 && (
              <VictoryLine
                data={[
                  { x: "AN2015", y: suma.AN2015 },
                  { x: "REG2017", y: suma.REG2017 },
                  { x: "PRES2018", y: suma.PRES2018 },
                  { x: "REG2021", y: suma.REG2021 },
                ]}
                style={{
                  data: { stroke: 'white', strokeWidth: 3},
                  labels:{
                    fontSize: 18,
                    fill: 'blue',
                    fontWeight: 'bold',
                    paddingTop: 30
                  },
                  tickLabels:{
                    padding: 30
                  } 
                }}
                labels = {({datum})=>datum.y}
              />
            )º  134567890'<
  }
        </VictoryChart>
    </View>
);
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: theme.colors.card,
    marginTop: 8,
    padding: 16,
    borderRadius: 12,
  },
  title: {
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 16,
    textAlign: "center",
    color: theme.colors.text,
  },
});

export default GraficaResultados;