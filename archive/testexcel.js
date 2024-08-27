const ExcelJS = require("exceljs");

// Créer une nouvelle instance de Workbook
const workbook = new ExcelJS.Workbook();

// Lire le fichier Excel
workbook.xlsx
  .readFile("alyfData.xlsm")
  .then(() => {
    // Accéder à la feuille nommée "DEV WEB"
    const worksheet = workbook.getWorksheet("DEV WEB");

    // Vérifier si la feuille existe
    if (!worksheet) {
      throw new Error('La feuille "DEV WEB" est introuvable.');
    }

    // Accéder à la cellule H1 et obtenir sa valeur
    let cell = worksheet.getCell("H1").value;
    //const formateur = cell.value;

    worksheet.getCell("H1").value = "Omari";

    workbook.xlsx.writeFile("alyfDev.xlsm");
    // Afficher la valeur
    console.log("La valeur de la cellule H1 est:", formateur);
  })
  .catch((error) => {
    console.error("Erreur lors de la lecture du fichier Excel:", error);
  });
