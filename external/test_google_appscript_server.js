

const doGet = (event = {}) => {
    const { parameter } = event;
    const { name = 'Anonymous', country = 'Unknown' } = parameter;
    const output = `Hello ${name} from ${country}`;
    // MailApp.sendEmail("ccaden21@gmail.com", "Hello", JSON.stringify(event))
    return ContentService.createTextOutput(output);
  }

// This gets the main spreadsheet, use this function as it guarantees that the sheet is correct.
// TODO: Maybe find a way to guarantee that this gets the right sheet without 'sheetName'
function GetSheet() 
{
  var sheetName = "robot_server";
  if ('sheet' in this) return this.sheet;
  var test = SpreadsheetApp.getActiveSpreadsheet();
  if (test.getName() == sheetName) {
    this.sheet = test;
    return this.sheet;
  }
  // else we will do more work to guarantee.
  var ret = DriveApp.getFiles();
  while (true) {
    if (!ret.hasNext()) return None;
    var file = ret.next();
    if (file.getName() == sheetName) {
      this.sheet = SpreadsheetApp.openById(file.getId());
      return this.sheet;
    }
  }
}

// This gets a sheet with a name.
function GetSheetWithName(name) 
{
  var sheet = GetSheet();
  var ret = sheet.getSheetByName(name);
  if (ret != null) {
    return ret;
  }
  Logger.log("Invalid name: ", name);
  throw ("Invalid sheet name: " + name);
}