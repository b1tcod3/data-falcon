import React, {useState} from 'react';
import {View, Text, StyleSheet, TouchableOpacity, Modal, ScrollView} from 'react-native';
import { theme } from '../theme';

const PickerSelect = ({items, selectedValue, onValueChange, placeholder}) => {
  const [modalVisible, setModalVisible] = useState(false);

  return (
    <View style={styles.container}>
      <TouchableOpacity 
      onPress={() => setModalVisible(true)} 
      style={styles.selectedContainer}>
        <ScrollView horizontal showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.scrollContent}
        >
          <Text style={styles.selectedText}>
            {selectedValue?.label || placeholder}
          </Text>
        </ScrollView>
      </TouchableOpacity>

      <Modal
        animationType="slide"
        transparent
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalBackground}>
          <View style={styles.modalContainer}>
            <ScrollView contentContainerStyle={styles.scrollContainer}>
              {items.map((item) => (
                <TouchableOpacity key={item.value} 
                onPress={() => {
                        onValueChange(item.value);
                        setModalVisible(false);
                }}
                style={styles.itemContainer}>
                  <Text 
                  style={styles.item}
                  numberOfLines={2}
                  ellipsizeMode="tail"
                  >{item.value}</Text>
                </TouchableOpacity>
              ))}
            </ScrollView>

            <TouchableOpacity onPress={() => setModalVisible(false)} style={styles.closeButton}>
              <Text style={styles.closeButtonText}>Cerrar</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: '100%',
    marginVertical: 8
  },
  selectedContainer: {
    backgroundColor: theme.colors.card,
    padding: 16,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: theme.colors.border,
  },
  selectedText:{
    color: theme.colors.text,
    fontSize: 16
  },
  scrollContainer: {
    padding: 16,
  },
  scrollContent: {
    alignItems: 'center',
    paddingVertical: 10
  },
  buttonText: {
    fontSize: 16,
    color: '#333',
  },
  modalContainer: {
    marginHorizontal: 20,
    backgroundColor: theme.colors.background,
    borderRadius: 12,
    maxHeight: '70%',
  },
  modalBackground: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: theme.colors.card,
  },
  
  itemContainer: {
    paddingVertical: 18,
    borderBottomWidth: 1,
    borderBottomColor: '#e9ecef',
  },
  closeButton: {
    padding: 16,
    borderTopColor: '#e9ecef',
    borderTopWidth: 1,
    alignItems: 'center',
  },
  closeButtonText: {
    fontSize: 16,
    color: '#3498db',
    fontWeight: '500',
  },
  item: {
    color: theme.colors.text,
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 18,
    paddingHorizontal: 20,
    borderBottomWidth: 1,
    flexDirection: 'row'
  }
});

export default PickerSelect;