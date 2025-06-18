import { theme } from "../theme";
import { StyleSheet} from "react-native";

export const appStyles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: theme.colors.background,
  },
  center: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
  },
  item: {
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
  },
  itemText: {
    fontSize: 18,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  scrollContainer: {
    flexGrow: 1,
    paddingBottom: 20,
    padding: 40,
  },
  container: {
    flex: 1,
    backgroundColor: theme.colors.background
  },
  contentContainer:{
    padding: 16,
    paddingBottom: 40
  },
  selectorCard:{
    backgroundColor: theme.colors.card,
    borderRadius: 12,
    padding: 16,
    marginBottom: 16
  },
  title: {
    fontSize: 24,
    marginTop: 50,
    marginLeft: 20,
    fontWeight: "bold",
    marginBottom: 20,
  },
  selectorLabel:{
    color: theme.colors.text,
    fontSize: 14,
    marginBottom: 8,
    opacity: 0.8
  }

});

