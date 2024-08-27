const xlsx = require("xlsx");
const winax = require("winax");

// Créer une instance d'Excel.Application et rendre Excel visible
const excel = new winax.Object("Excel.Application");
excel.Visible = true;

// Charger le fichier Excel
const fichierExcel = xlsx.readFile("alyfData.xlsm");

// Accéder à une cellule spécifique (par exemple, H1 de la feuille "DEV WEB")
const sheetName = "DEV WEB";
const cellAddress = "H1";

if (fichierExcel.Sheets[sheetName]) {
  const cellValue = fichierExcel.Sheets[sheetName][cellAddress].v;
  console.log(cellValue);

  // Ouvrir le fichier dans l'instance Excel pour exécuter la macro
  const workbook = excel.Workbooks.Open(__dirname + "\\alyfData.xlsm");

  // Sélectionner la feuille sur laquelle la macro doit être exécutée
  const feuille = workbook.Sheets("DEV WEB");
  feuille.Activate();

  // Exécuter la macro spécifiée
  excel.Run("Feuil2.generer_calendrier");

  // Fermer le fichier sans sauvegarder
  workbook.Close(false);
} else {
  console.log(`La feuille "${sheetName}" n'existe pas dans le fichier.`);
}

// Fermer l'application Excel
excel.Quit();
