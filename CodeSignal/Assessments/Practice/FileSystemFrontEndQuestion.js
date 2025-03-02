IDE
To customize the editor settings and see the editor hotkeys, check out the Settings tabon the left sidebar.

See the README tab for more information about the environment and test run verdicts.

The IDE will automatically install the development environment and required packages from package.json. Feel free to modify the package.json file to include additional packages as needed. You can use the console to stop or restart your application whenever you want. The live preview pane will update as you work to reflect the current state of your application. If you close the console and want to restart the application, run the command npm start.

If needed, you can hard reset the environment by clicking on the circular reset code icon () on the top right of the IDE. Note that your progress will not be saved, so please be careful when using this.

Prettier
Please note that prettier is already included in package.json. For formatting the code, run the command npm run prettier in the console.

Debugging
If you add debugging output to the console in your components, please check your browser's debug console for output messages.

Feel free to browse the project workspace. All necessary component files have been created for you.

Scenario
You are given a page with a clock. Your task is to implement the logic for buttons to increment and decrement the hours and minutes.

The time should be displayed in HH:MM 24-hour format. For example, 23:59, 08:00, 07:32.

The initial state of the clock should be 00:00.

Actions should be cycled; if you have 23:58 on the clock and press up for hours, the resulting time should be 00:58.

Minutes and hours should be changed separately.

Tests
Unit tests are provided in the test/functionalTests.test.js file. To run the tests, click the blue In Terminal or Structured button.
You may use test/sample.test.js to write your own tests, which will also be included in the test runs.
If you would like to include debugging output to the console in your tests, use the In Terminal option to receive the raw test output.
When working on a scored certification, partial credit will be granted for each unit test passed, so press Submit often to run tests and receive partial credits for passed tests.
    


UNIT_TEST


Clock updater
✔ has all four buttons (78ms)
✔ has the default state
✔ successfully increases the hour
✔ successfully decreases the hour
✔ successfully increases the minute
✔ successfully decreases the minute
✔ makes the minutes `59` when decreased from `00`
✔ makes the minutes `59` when increased from `59` (57ms)
✔ makes the hours `23` when decreased from `00` (45ms)
✔ makes the hours `00` when increased from `23`
✔ stays the same after increasing the hours 24 time and decreasing the minutes 60 time (1664ms)
✔ successfully makes the time `16:08` (318ms)

Sample test
✔ sample test


13 passing (8s)


import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  hours = '00';
  minutes = '00';

  handleHoursUpButtonClick() {
    // TODO: implement this
    let h = parseInt(this.hours, 10);
    h = (h+1)% 24;
    this.hours = this.formatTime(h);
  }

  handleHoursDownButtonClick() {
    // TODO: implement this
    let h = parseInt(this.hours, 10);
    h = ( h - 1 + 24) % 24;
    this.hours = this.formatTime(h);
  }

  handleMinutesUpButtonClick() {
    // TODO: implement this
    let m = parseInt(this.minutes, 10);
    m = ( m + 1 ) % 60;
    this.minutes = this.formatTime(m);
  }

  handleMinutesDownButtonClick() {
    // TODO: implement this
    let m = parseInt(this.minutes, 10);
    m = (m - 1 + 60) % 60;
    this.minutes = this.formatTime(m);
  }
  
  private formatTime(value: number): string {
    return value < 10 ? `0${value}` : `${value}`;
  }
  
}

