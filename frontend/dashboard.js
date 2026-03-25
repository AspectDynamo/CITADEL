// dashboard.js

// Function to display current date and time in UTC
function displayCurrentDateTime() {
    const now = new Date();
    const utcDateTime = now.toISOString().replace('T', ' ').substring(0, 19);
    console.log('Current Date and Time (UTC):', utcDateTime);
}

// Call the function to display the date and time
displayCurrentDateTime();

// Additional dashboard functionality can be added here.
// Examples:
// 1. Fetch user data
// 2. Display dashboard metrics
// 3. Create interactive charts

