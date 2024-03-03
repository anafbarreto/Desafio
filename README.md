# Desafio
Create API system that receives denormalized data, performs processing, and returns it in a normalized json file. <br>

# Index
* [Data example](#application-result)
* [Project description](#project-description)
* [Technologies used](#technologies-used)
* [Tests](#tests)
* [Project execution](#project-execution)
* [Test execution](#test-execution)
* [Thanks](#thanks)

### Application result
Input data: <br><br>
<img src=Images/image.png>

Output data: <br><br>
<img src=Images/image-5.png>

### Project description
The application has two main routes: <br>
1. '/process' route: which can receive one or more files as a query parameter, reading and processing the data. <br>
2. Route '/display': allows you to view the processed data, and filter it based on optional parameters, such as order ID, start date and end date. <br>

Main functions: <br>
- `Process_data(file_paths)`: processes data from the provided files. Extracts information such as user ID, name, order ID, product ID, total, and purchase date. <br>
- `Filter_data(user_data, order_id, start_date, end_date)`: filters user data based on the parameters provided, such as order ID, start date and end date. <br>

### Technologies used
- Flask: Using the Flask web framework due to its simplicity and flexibility. Flask allowed you to create API routes quickly and easily. <br>
- Jsonify: Flask's jsonify function was used to format API responses in JSON in a simple and direct way. <br>
- Datetime: The standard Python datetime library was used to manipulate dates. Allowing you to convert and validate dates as needed during data processing. <br>
- Pytest: The pytest testing framework was chosen due to its ease of use and powerful testing capabilities. It has clear and concise writing to validate the application's behavior. <br>

Architectural Patterns: <br>
- MVC (Model-View-Controller) pattern: Although it is not a complete MVC framework, it has a similar approach by dividing the application into model, view and control layers. This allows you to keep the code organized and separated into distinct components. <br>
- RESTful API: The application follows the principles of a RESTful API, where operations are mapped to HTTP methods (GET, POST, etc.) and resources are accessed through URLs. <br>
- Separation of Responsibilities: Seeking to maintain a clear separation of responsibilities in the code, where each component (such as API routes, business logic and data manipulation) has a specific and well-defined function. <br>

The choice of technologies and standards were made with a view to simplicity, the volume of data used in testing and maintenance of the application. <br>

### Tests
1. The `test_process_data` test checks the behavior of the '/process' route for different scenarios such as no file provided and non-existent file.
2. The `test_display_data` test checks the behavior of the '/display' route for different scenarios, such as no data processed yet, order ID not found, and invalid dates.

Code and test coverage: 100%** (Coverage Report) <br>
** Not taking into account the import and function definition lines. <br>

### Project Execution
The environment with the technologies necessary to execute the project are already in the .venv folder of this repository. <br>
In case of doubt, a file with all the libraries used and how to install them is available in the repository in the "libraries" folder.

1. In the top corner, make a fork. <br><br>
<img src=Images/image-1.png>

2. Open the Challenge folder in your editor and open the files described in .gitignore. <br><br>
<img src=Images/image-2.png>

3. To run the application, in the terminal use: flask --app app run <br><br>
<img src=Images/image-3.png>
Your local server can be opened in applications like Postman, in extensions like Thunder Client and in the browser itself like Edge and Chrome**. <br>
** Chrome does not have Json output in the data so the visualization may be different. <br>

4. To send a file you can use the route: http://localhost:porta/process?file_paths=nome_do_arquivo.txt
To add more files, simply fill in &file_paths=arquivo2.txt and so on. <br><br>
<img src=Images/image-6.png> <br> 

5. Display data: http://localhost:port/display. This functionality also allows data to be filtered by order_id and date. <br>
Examples: <br>
http://localhost:porta/display?order_id=751 <br>
http://localhost:porta/display?start_date=2021-01-01 <br>
http://localhost:porta/display?end_date=2021-12-31 <br>
http://localhost:porta/display?start_date=2021-01-01&end_date=2021-12-31 <br><br>
<img src=Images/image-7.png>


### Test execution
1. In the terminal use: pytest test.py to generate the test report. The display will be on the terminal itself.
2. Coverage is enabled to generate HTML output, showing test and application coverage, which can be accessed from the 'Index.html' file in the 'Coverage_html_report' folder in the directory. <br><br>
<img src=Images/image-8.png>
Another option is to execute the command: coverage report -m, so the visualization will also be directly in the terminal.<br><br>
<img src=Images/image-9.png>


### Thanks
Em pt-br, fazer esse teste foi divertido e eu precisei assistir boas aulas durante o processo. Obrigada! <br><br>
![catprog](https://github.com/anafbarreto/Desafio/assets/44984838/87f17484-6a56-4b34-b52e-c3ecb980edd0)







