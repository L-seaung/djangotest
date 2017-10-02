###### No.1

###### create directive

```
// using command create directive
ng generate directive directive-name
```

```
// manual create directive
import { Directive } from '@angular/core';

@Directive({
  selector: '[directive-name]'
  })
  export class CustomeDirective {
    // code statement
  }
```

```
// using custom directive in template
<div #directive-name>
</div>
```

> this is all ...
