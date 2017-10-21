import { ModuleWithProviders }   from '@angular/core';
import { Routes, RouterModule }   from '@angular/router';

import { MainComponent }  from './main.component';
import { CreateComponent } from "./create.component";
import { ErrorComponent } from './error.component';
import { RoutePlanComponent } from './routeplan.component';
import { RoutePlansComponent } from './routeplans.component';
import { MypageComponent } from './mypage.component';
import { LoginComponent } from './login.component';
import { SignupComponent } from './signup.component';
import { UserComponent } from './user.component';
import { SpotComponent } from './spot.component';


const myRoutes = [
  { path: 'create', component: CreateComponent },
  { path: 'route-plan/:id', component: RoutePlanComponent },
  { path: 'route-plans', component: RoutePlansComponent },
  { path: 'mypage', component: MypageComponent },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'user/:id', component: UserComponent },
  { path: 'spot/:id', component: SpotComponent },
  { path: '', component: MainComponent },
  { path: '**', component: ErrorComponent }
  //{ path: '**', redirectTo: '/' }
];

export const MY_ROUTES: ModuleWithProviders = RouterModule.forRoot(myRoutes);
