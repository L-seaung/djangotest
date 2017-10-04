##### No.1

> dependecy injection (DI) is a core concept of angular 2+ and allows a class receive dependencies from another class. Most of the time in Angular, dependecy injection is done by injecting a service class into a component or module class.
here's for example how you would define an injectable service. pay special attention to the highlingted parts:

```
import { Injectable} from '@angular/core';

@Injectable()
export class PopcornService {
  constructor() {
    console.log("popcorn has been injected!");
  }

  cookPopcorn(qty) {
    console.log(qty, "bags of popcorn cooked!");
  }
}

// and here's  how you would inject our popcorn service it in a component:

import { Component } from '@angular/core';
import { PopcornService } './popcorn.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  provicers: [PopcornService]
  })
  export class AppComponent {
    constructor(private popcorn: PopcornService) {}

    cookIt(qty) {
      this.popcorn.cookPopcorn(qty);
    }
  }

  // the cookIt() method in the template calls the cookPopcorn() method in the injected service.
  Let's make use of our cookIt() method in our template:

  <input type="number" #qty placeholder="how many bags?">
  <button type="button" (click)="cookIt(qty.value)">
  cookIt
  </button>
```
