import { DebugElement, NO_ERRORS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';

import { AppComponent } from './app.component';

describe('AppComponent', function () {
  let des: DebugElement[];
  let comp: AppComponent;
  let fixture: ComponentFixture<AppComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ AppComponent ],
      //schemas:      [ NO_ERRORS_SCHEMA ]
    });

    fixture = TestBed.createComponent(AppComponent);
    comp = fixture.componentInstance;
    des = fixture.debugElement.queryAll(By.css('a'));
  });

  it('<a>要素の個数を確認', () => {
    fixture.detectChanges();
    expect(des.length).toEqual(3);
  });
});