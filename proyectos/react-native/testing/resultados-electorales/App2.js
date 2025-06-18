//import React,{ useState } from "react";
import { StatusBar } from 'expo-status-bar';
import { ScrollView, StyleSheet, View } from 'react-native';
//import MunicipioSelector from './components/MunicipioSelector';
//import ParroquiaSelector from './components/ParroquiaSelector';

export default function App() {
  // const [selectedMunicipio, setSelectedMunicipio] = React.useState(null);
  // const [selectedParroquia, setSelectedParroquia] = React.useState(null);
  //const [municipio, setMunicipio] = React.useState(null);  

  return (
    <View style={styles.container}>
      <Text style={styles.label}>Resultados Electorales</Text>
    </View>
    // <ScrollView contentContainerStyle={styles.container}>
    //   <View style={styles.section}>
    //     <Text style={styles.label}>Municipio:</Text>
    //     <MunicipioSelector onSelect={setSelectedMunicipio}/>
    //   </View>
    //   <View style={styles.section}>
    //     <Text style={styles.label}>Parroquia:</Text>
    //     <ParroquiaSelector 
    //     municipio={selectedMunicipio}
    //     onSelect={setSelectedParroquia}
    //     />
    //   </View>
    //   {selectedParroquia && (
    //     <View style={styles.section}>
    //       <Text style={styles.label}>Selected Parroquia:</Text>
    //       <Text>{selectedParroquia}</Text>
    //     </View>
    //   )}
    //   <StatusBar style="auto" />
    // </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  label: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
    color: '#333',
    fontWeight: '500',
  },
  section: {
    marginTop: 50,
    padding: 20,
    backgroundColor: '#fff',
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
});
