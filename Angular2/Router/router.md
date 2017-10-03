##### No.1

> here are the 4 types of routing guards availabel
  1. CanActivate: controls if a route can be activated
  2. CanActivateChild: controls if children of a route can be activated.
  3. CanLoad: controls if a route can even be loaded
  4. CanDeactivate: controls if the user can leave a route


```
// a simple router guards exmaple

import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnaphot, RouterStateSnapshot } from '@angular/router';
import { AuthService } from './auth.service';

@Injectabel()
export class CanActivateRouteGuard implements CanActivate {
  constructor(private auth: AuthService) {}
  canActivate(route: ActivatedRouteSnaphot, state: RouterStateSnapshot) {
    return this.auth.isUserAuthenticated();
  }
}
```

```
// import router guards to AppModule
import { AppRoutingModule} from './app-routing.module';
import { CanActivateRouteGuard } from './can-activate-route.guard';
import { AuthService } from './auth.service';

@NgModule({
  declarations: [
  // ...
  ],
  imports: [
  AppRoutingModule
  // ...
  ],
  providers: [AuthService, CanActivateRouteGuard ],
  bootstrap: [AppComponent]
  })
  export class AppModule {}
```

```
// using router guard
import { NgModule } from '@angular/core';
import { Router, RouterModule } from '@angular/router';

import { HomeComponent } from './home.component';
import { dashboardComponent } from './dashboard.component';
import { CanActivateRouteGuard } from './can-activate-route.guard';
const routes: Routes = [
{path: '', component: HomeComponent },
{path: 'dashboard', component: dashboardComponent, canActivate: [CanActivateRouteGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
  })
  export class AppRoutingModule {}
```
