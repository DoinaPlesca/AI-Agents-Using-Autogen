## **1. Project Setup**

### 1.1 Create your project folder

```bash
mkdir autogen_assignment2
cd autogen_assignment2
````

### 1.2 Create a virtual environment (Python 3.12)
```bash -powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate
````

### 1.3 Check python version inside venv
```bash -powershell
python --version
````

## 2. Install the required dependencies (inside venv)
```bash -powershell
C:\Users\xxxxx\autogen_assignment2\venv\Scripts\python.exe -m pip install --upgrade pip
````
```bash -powershell
pip install "autogen-agentchat @ git+https://github.com/patrickstolc/autogen.git@0.2#egg=autogen-agentchat"
pip install autogen==0.3.1
pip install mistralai==1.2.3
pip install ollama==0.3.3
pip install fix-busted-json==0.0.18
````

### 2.1 Check instalation
```bash -powershell
pip list
````
You should now see the following packages installed:

1. [ ] autogen 0.3.1
2. [ ] 
3. [ ] autogen-agentchat 0.2.x
4. [ ] 
5. [ ] mistralai 1.2.3
6. [ ] 
7. [ ] ollama 0.3.3
8. [ ] 
9. [ ] fix-busted-json 0.0.18
10. [ ] 
11. [ ] and other dependencies# AI-Agents-Using-Autogen
