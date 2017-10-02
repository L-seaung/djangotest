####  No.1

###### create component

```
// using command
ng generate component component-name
```

```
// manual create component

for example

import { Component } from '@angular/core';

@Component({
  selector: 'selector-name',
  templateUrl: './template-path/template-name',
  // or template: `template content`
  styleUrls: ['./style-path/style-name']
  // or style: `[style....]`
  })
  export class Component-Name {
    // attribute and methods
    constructor() {

    }
  }
```

> this is all ...
