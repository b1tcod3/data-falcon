import { ScrollView, StyleSheet, View, Text } from 'react-native';
import React from "react";
import { StatusBar } from 'expo-status-bar';
import MunicipioSelector from './components/MunicipioSelector';
import ParroquiaSelector from './components/ParroquiaSelector';
import CentroSelector from './components/CentroSelector';
import GraficaResultados from './components/GraficaResultados';
import { appStyles } from './styles/appStyles';


export default function App() {
  const [selectedMunicipio, setSelectedMunicipio] = React.useState(null);
  const [selectedParroquia, setSelectedParroquia] = React.useState(null);
  const [selectedCentro, setSelectedCentro] = React.useState(null);

  return (
    <ScrollView 
      style={appStyles.container}
      contentContainerStyle={appStyles.contentContainer}
    >
      <View style={appStyles.selectorCard}>
        <Text style={appStyles.selectorLabel}>Municipio</Text>
        <MunicipioSelector onSelect={setSelectedMunicipio}/>
      </View>

      <View style={appStyles.selectorCard}>
        <Text style={appStyles.selectorLabel}>Parroquia</Text>
        <ParroquiaSelector 
          municipio={selectedMunicipio}
          onSelect={setSelectedParroquia}
          />
      </View>
      
      <View style={appStyles.selectorCard}>
        <Text style={appStyles.selectorLabel}>Centro Electoral</Text>
        <CentroSelector 
        municipio={selectedMunicipio}
        parroquia={selectedParroquia}
        onSelect={setSelectedCentro}
        />
      </View>
      
      <GraficaResultados 
        municipio={selectedMunicipio}
        parroquia={selectedParroquia}
        centro={selectedCentro}
        />
      
      <StatusBar style="auto" />
    </ScrollView>
  );
}

