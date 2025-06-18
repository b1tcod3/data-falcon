import { loadData } from './dataLoader.js';
import * as FileSystem from 'expo-file-system';
import { Asset } from 'expo-asset';
import { Platform } from 'react-native';

export async function getMunicipios() {

    try {
        if (Platform.OS === 'web') {
            pathFile = '/municipios.csv';
            data = loadData
        }
        else{
            const asset = Asset.fromModule(filePath);
            await asset.downloadAsync();

            const csvContent = await FileSystem.readAsStringAsync(asset.localUri || asset.uri);
            const data = await loadData(pathFile);    
        }
        
        return {
            success: true,
            data: data,
            error: null,
        };
    }
    catch (error) {
        console.error('Error loading municipios:', error);
        return {
            success: false,
            data: null,
            error: {
                message: 'Error loading municipios',
                code: error.code || 'UNKNOWN_ERROR',
            }
        };
    }

}