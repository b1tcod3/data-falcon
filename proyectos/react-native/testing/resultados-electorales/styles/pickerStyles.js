import { theme } from "../theme";
import { StyleSheet} from "react-native";

export const pickerSelectStyles = StyleSheet.create({
  inputIOS: {
    fontSize: 16,
    backgroundColor: '#363636',
    paddingVertical: 12,
    paddingHorizontal: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 4,
    color: theme.colors.text,
    paddingRight: 30, // to ensure the text is never behind the icon
  },
  inputAndroid: {
    fontSize: 16,
    paddingVertical: 8,
    paddingHorizontal: 10,
    backgroundColor: '#363636',
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 4,
    color: theme.colors.text,
    paddingRight: 30, // to ensure the text is never behind the icon
  },
  placeholder: {
    color: theme.colors.secondary
  },
  selectorIcon:{
    backgroundColor: theme.colors.primary,
    width: 20,
    height: 20,
    borderRadius: 10,
    marginRight: 10
  }
});