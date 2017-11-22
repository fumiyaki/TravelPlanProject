import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule, RequestOptions, XSRFStrategy, CookieXSRFStrategy } from '@angular/http';
import { FormsModule }  from '@angular/forms';

import { MY_ROUTES }   from './app.routing';

import { AppComponent }   from './app.component';
import { MainComponent }  from './main.component';
import { CreateComponent }  from './create.component';
import { ErrorComponent } from './error.component';
import { RoutePlanComponent } from './routeplan.component';
import { RoutePlansComponent } from './routeplans.component';
import { MypageComponent } from './mypage.component';
import { LoginComponent } from './login.component';
import { SignupComponent } from './signup.component';
import { UserComponent } from './user.component';
import { SpotComponent } from './spot.component';

import { TruncatePipe } from './truncate.pipe'

@NgModule({
  imports:      [ BrowserModule, MY_ROUTES, FormsModule, HttpModule ],
  declarations: [ AppComponent, MainComponent,
    CreateComponent, ErrorComponent, RoutePlanComponent, RoutePlansComponent, MypageComponent, LoginComponent, SignupComponent, UserComponent, SpotComponent, TruncatePipe ],
  bootstrap:    [ AppComponent ],
  //XSRF対策
  providers:    [
    { provide: XSRFStrategy,
       useValue: new CookieXSRFStrategy('CSRF-TOKEN', 'X-CSRF-TOKEN') }
  ]
})
export class AppModule { }
