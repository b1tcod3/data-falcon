import React,{useState,useEffect} from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { getMunicipios } from './lib/municipios';

export default function App() {

  const [municipios, setMunicipios] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMunicipios = async () => {
      try {
        const response = await getMunicipios();
        if (response.success) {
          setMunicipios(response.data);
        } else {
          setError(response.error);
        }
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    
    };

    fetchMunicipios();
  }, []);
  
  console.log('Municipios:', municipios);

  return (
    <SafeAreaProvider>
      <View style={styles.container}>
        <Text>Open up App.js to start working on your app!</Text>
        <StatusBar style="auto" />
        {loading && <Text>Loading..kk.{{municipios}}</Text>}
        {error && <Text>Error: {error.message}</Text>}
        <Text>Longitud:{municipios.length}</Text>
        {municipios.length > 0 && (
          <View>
            <Text>Municipios:</Text>
            {municipios.map((municipio) => (
              <Text key={municipio.municipio}>{municipio.municipio}</Text>
            ))}
          </View>
        )}
      </View>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
