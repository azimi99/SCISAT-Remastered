[About](#-SCISAT-project-remastered)



# SCISAT project remastered

Initially designed for a CSA challenge. SCISAT posed lots of interesting challenges, both scientific and technical. At the time of
the competition, our team lacked the required technical knowledge to truly exhibit the power of data. The remastered project addresses
this exact issue.
SCISAT collects atmospheric data on varius gases. Our project concentrates on visualizing the data from the Ozone gas. 
Along with the visualization we have also provided a public api endpoint for everyone wishing to use the data we have collected.

## Definition of Roles

1. Alireza Azimi -> BackEnd Development
2. Shayan Khorassani -> FrontEnd Development
3. Haren Venket -> Data Analyst

## Run the project locally

To run the project you need to have `npm` and `node` installed. 
Enter the project directory and run `$ npm i` to install all the required dependancies.

Once done, you can run `$ node index.js` to initiate localhost. The project will run on port 3000.
Enter port 3000 from a browser.

## Elements used in the project

Our project incorporates some of the latest web development technologies.<br/>
Our Frontend is developed using HTML5, CSS, jQuery and JavaScript.<br/>
Our Backend is implemented in node.js using technologies like express.js and mongoose.<br/>
Our database is implemented using MongoDB Atlas.<br/>
Our data has been processed from data provided by the Canadian government, for the SCISAT project.<br/>

## API Usage
There is one main endpoint:
/Data<br/>
Here's a sample usage of the api:
`Data?q=2004-03`

This api call will return all data recorded in the time period "2004-03".<br/>
You can query for various dates in the 2004-03 to 2010-12 range. Pass the query date string to the paremter `q` as shown in the example.<br/>

## Live Demo

Here's a link to our demo:
https://sheltered-dusk-02570.herokuapp.com/

Old project repository:
https://github.com/DJMaest/SCISAT
<br />
Looking at this definitely shows how far we've come
