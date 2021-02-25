

const doGet = (event = {}) => {
    const { parameter } = event;
    const { blob = "" } = parameter;
    var partsArray = blob.split(' ');
    if(partsArray[0] == "computer"){
      if(blob != ""){
        log_blob_c(blob);
      }
    
      read_blob_c();
      return ContentService.createTextOutput(read_blob_c());
      
      return ContentService.createTextOutput("hi");
    }
    if(partsArray[0] == "robot"){
      if(blob != ""){
        log_blob_r(blob);
      }

      
    
      read_blob_r();
      return ContentService.createTextOutput(read_blob_r());
      
      return ContentService.createTextOutput("hi");
    }
    return ContentService.createTextOutput("hi");
  }

// This gets the main spreadsheet, use this function as it guarantees that the sheet is correct.
// TODO: Maybe find a way to guarantee that this gets the right sheet without 'sheetName'
function GetSheet() 
{
  var sheetName = "QG Webserver";
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

function log_blob_c(string){
  var write_to_sheet = GetSheetWithName("sheet1");
  write_to_sheet.getRange(1,1).getCell(1,1).setValue(string) // This is the cell the computer writes too\

}

function read_blob_c(){
  var read_sheet = GetSheetWithName("sheet1");
  return read_sheet.getRange(2,1).getCell(1,1).getValue() //Cell 2B this would be the cell computer reads from.
}

function log_blob_r(string){
  var write_to_sheet = GetSheetWithName("sheet1");
  write_to_sheet.getRange(2,1).getCell(1,1).setValue(string) // This is the cell the robot writes too

}

function read_blob_r(){
  var read_sheet = GetSheetWithName("sheet1");
  return read_sheet.getRange(1,1).getCell(1,1).getValue() //This cell would be the cell robot would read too.
}

function test_write(){
  log_blob_c("Hello")
}

function test_read(){
  return ContentService.createTextOutput(read_blob_c())
}




