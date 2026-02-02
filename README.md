# Description
Test Automation Framework using Selenium WebDriver and Robot Framework

# Capabilities
- ✅ Allure.html reporter
- ✅ Keyword or Gherkin/BDD Test Case format
- ✅ Parallelized execution on Test Case level using Pabot
- ✅ Gitlab CI ready
- ✅ Execute via CMD (robot runner)

# Setup guide
1. **Install [Python 3.11.8](https://www.python.org/downloads/release/python-3118/)**
2. **Set environment variables:**
    - On **Windows**, go to *Control Panel > System and Security > System > Advanced system settings*
        - Click **Environment Variables**
        - Under **System variables**, select **Path** and click **Edit**
        - Add `C:\Users\(user)\AppData\Local\Programs\Python\Python311` and `C:\Users\(user)\AppData\Local\Programs\Python\Python311\Scripts`
3. **Set .venv as Python interpreter**
4. **Run Tests**
    - via `Terminal`:
        - `robot --pythonpath . --outputdir ./allure-report .\tests\demo_planittesting.robot`

# Others
- Set TEST_URL key in as a local Environment Variable