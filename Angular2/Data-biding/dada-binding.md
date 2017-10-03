###### No.1

> Data binding is a core concept in Angular and allows to define communication between a component and the DOM, making it easy to define interactive applications without worrying about pushing and pulling data. there are four forms of data binding and they differ in the way the data is flowing.

```
// from the Component to the DOM

Interpolation: {{value}}

this adds the value of a property from the Component

<li>Name: {{user.name}}</li>
<li>Email: {{user.email}}</li>
```

```
// property binding: [property]="value"

with property binding, the value is passed from the component to the specified property, which can often be a simple html attribute:
<input type="email" [value]="user.email">

```

```
// building in attribute

for example:
<div [style.background-color]="selectedColor">
<div [class.selected]="isSelected">
```

> from the DOM to the Component

```
// event binding:(event)="function"

when a specific DOM event happens (eg:click, change, keyup), call the specific method in the component. In the example below, the cookBacon() method from the component is called when the button is clicked:
<button (click)="cookBacon()"></button>
```


```
// tow-way
tow-way data binding: [(ngModel)]="value"

<input type="email" [(ngModel)]="user.email">
```
