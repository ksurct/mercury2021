

const doGet = (event = {}) => {
    const { parameter } = event;
    const { name = 'Anonymous', country = 'Unknown' } = parameter;
    const output = `Hello ${name} from ${country}`;
    // MailApp.sendEmail("ccaden21@gmail.com", "Hello", JSON.stringify(event))
    return ContentService.createTextOutput(output);
  }