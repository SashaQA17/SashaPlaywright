from playwright.async_api import expect
from playwright.async_api import async_playwright
import pytest



@pytest.mark.asyncio
async def test_first():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://demoqa.com/')
        await expect(page).to_have_title('DEMOQA')

@pytest.mark.asyncio
async def test_second():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://demoqa.com/')
        await expect(page).to_have_title('DEMOQA')
        elements_btn = page.locator('//h5[text()="Elements"]')
        await elements_btn.click()
        await expect(page).to_have_url('https://demoqa.com/elements')

@pytest.mark.asyncio
async def test_third():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://demoqa.com/')
        await expect(page).to_have_title('DEMOQA')
        form_btn = page.locator('//h5[text()="Forms"]')
        await form_btn.click()
        await expect(page).to_have_url('https://demoqa.com/forms')

@pytest.mark.asyncio
async def test_fourth():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://demoqa.com/')
        await expect(page).to_have_title('DEMOQA')
        alerts_btn = page.locator('//h5[text()="Alerts, Frame & Windows"]')
        await alerts_btn.click()
        await expect(page).to_have_url('https://demoqa.com/alertsWindows')

