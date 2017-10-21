import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
    templateUrl: `./templates/menu.component.html`,
})
export class AppComponent {
  user_id = '';

  ngOnInit(){
    this.user_id = localStorage.getItem('token');
  }
  logout(){
    localStorage.removeItem('token');
    location.href = "./";
  }
}
