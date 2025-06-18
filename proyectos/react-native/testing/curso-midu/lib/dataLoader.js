import * as FileSystem from 'expo-file-system';
import Papa from 'papaparse';
import { Platform } from 'react-native';


export const loadData = async (filePath) => {
    if (Platform.OS === 'web') {
        // If the platform is web, use fetch to get the file
        try{
            const response = await fetch(filePath);

            const text = await response.text();

            return parseCsv(text);
        }
        catch(error){
            console.error('Error loading data:', error);
            throw error;
        }

    }
    try{
        // If the platform is not web, use FileSystem to get the file
        const csvString = await FileSystem.readAsStringAsync(filePath);

        return parseCsv(csvString)
    }
    catch (error) {
        console.error('Error loading data:', error);
        throw error;        
    }
}

//parse the CSV data
const parseCsv = (csvString) => {
    return new Promise((resolve, reject) => {
    Papa.parse(csvString, {
        header: true,
        skipEmptyLines: true,
        complete: (result) => resolve(result.data),
        error: (error) => reject(error),
    });
});
};
