import { browser, element, by } from 'protractor';

describe('QuickStart E2E Tests', function () {

  let expectedMsg = 'Hello Angular';

  beforeEach(function () {
    browser.get('');
  });

  it('遷移のテスト', function() {
    expect(browser.getTitle()).toEqual('Angular QuickStart');
    expect(element(by.css('h2')).getText()).toEqual('メインページ');

    element(by.linkText('Exampleページ')).click();
    expect(element(by.css('h2')).getText()).toEqual('Example');
  });
});
