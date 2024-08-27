const winax = require("winax");

try {
  // Créer une instance de l'application Excel
  const excel = new ActiveXObject("Excel.Application");
  excel.Visible = true; // Rendre Excel visible

  // Ouvrir le fichier Excel
  const workbook = excel.Workbooks.Open(
    "C:\\Users\\nasse\\Test-fichier-excel\\alyfData.xlsm"
  );

  // Exécuter la macro
  const macroName = "Feuil2.generer_calendrier"; // Assurez-vous que 'Module1' est le nom correct du module
  // Utilisez le nom complet de la macro si nécessaire
  excel.Run(macroName);

  // Sauvegarder et fermer le fichier
  workbook.Save();
  workbook.Close(false);

  // Quitter Excel
  excel.Quit();
} catch (err) {
  console.error("Erreur lors de l'exécution de la macro :", err);
}
