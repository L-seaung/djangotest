###### No.1

> Query parameters in angular allow for passing optional parameters across any route in the application.


1. Query params with Router.navigate

//  if you are navigating to the route imperatively using Router.navigate, here's how to pass in query params:

```
goProducts() {
  this.router.navigate(['/products', { queryParams: { order: 'popular'}}]);
}

// result http://http://localhost:4200/products?order=popular

// you can also provide multiple query params like this:

goProducts() {
  this.router.navigate(['/products'], { queryParams: { order: 'popular', 'price-range': 'not-cheap'}});
}

// and the url looks like this:
   http://localhost:4200/products?order=popular&price-range=not-cheap
```

2. Preserve or Merge query params with queryParamsHanding

> by default the query parameters are lost on any subsequent navigation action. to prevent this, you can set queryParamsHanding to either preserve or merge. let's say we are on the products route and want to route the user to the users page while keeping the query params.

```
goUsers() {
  this.router.navigate(['/users'], { queryParamsHanding: 'preserve'});
}

// we can merge instead of preserve if you're also passing new query params to the users route:

goUsers() {
  this.router.navigate(['/users'], { queryParams: {filter: 'new'}, queryParamsHanding: 'merge'});
}

// the result url:
   http://localhost:4200/users?order=popular&filter=new
```

// query params with routerLink

> if instead you are using the RouterLink directive to navigate to the route, here's how you would set query params:

```
<a [routerLink]="['/products']" [queryParams]="{order: 'popular'}">
Products</a>

// and if you want to preserve or merge query params on subsequent navigation:

<a [routerLink]="['/products']" [queryParams]="{ order: 'popular'}">
products
</a>

and if you want to preserve or merge query params on subsequent navigation:

<a [routerLink]="['/users']" [queryParams]="{filter: 'new'}" queryParamsHanding="merge">
users
</a>
```

3. accdssing query param values

> given the following route Url:

```
http://localhost:4200/products?order=popular

// we can sccess the order query patam link this:
import { ActivatedRoute } from '@angular/router';
import 'rxjs/add/operator/filter';

@Component({...})
export class ProductComponent implements OnInit {
  order: string;
  constructor(private route: ActivatedRoute) {}
  ngOnInit() {
    this.route.queryParams
    .filter(params => params.order)
    .subscribe(params => {
      console.log(params); // {order: "popular"}
      this.order = params.order;
      console.log(this.order); // popular
      });
  }
}
```

> there's also queryParamMap, which returns an observable with a paramMap object. Given the follwing route URL:

```
http://localhost:4200/products?order=popular&filter=new

this.route.queryParamMap.subscribe(params => {
  this.orderObj = {...params.keys, ...params};
  });

  we used the object spread operator here, and this is the resulting shape of the
  data in orderObj:
  {
    "0": "order",
    "1": "filter",
    "params": {
      "order": "popular",
      "filter": "new"
    }
  }

```
