# shopify
## Step 1:
Create a new environment in anaconda with 


`conda create --name shopify`


and activate your environtment with 


`conda activate shopify`.
## Step 2:
Install FastApi and Uvicorn in your machine with the commands

`pip install fastapi`


`pip install "uvicorn[standard]"`

## Step 3
Install the python packages numpy,pandas and python multipart with the following codes.


`pip install python-multipart`


`pip install pandas`


`pip install numpy`

## Step 4:
Make sure the terminal is running in the same folder as the repository.Run the program using the command 


`uvicorn main:app --reload`

## Step 5:
Go to http://127.0.0.1:8000/docs# on your browser and click on try it out.

Click on `choose file` and upload the dataset from your device.
You should find the results.


![The window should look like this](https://github.com/ninienowrin/shopify/blob/main/shopify.png)
