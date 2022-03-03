# TravelXp.com Travel Agency


## Description

**TravelXp.com Travel Agency** and **TravelXp.com Visas** communicate completely via events. First **TravelXp.com Travel Agency** sends visa applications 
for those travellers that require visas to visit given country, next based on visa application evaluation, **TravelXp.com Visas** sends back 
the response with the visa processing outcome - approved or rejected.

## Theme
The main motive and theme of starting this service is to provide a 
better and lovely experience for all the travellers 
who love to roam around the world 🌏 at a very cheap and feasibl cost with 100 % privacy and security.


## Activities to perform

* Create project with following extensions
	* TravelXp.com
	* Openair.com
* Create data model
	* Traveller
	* Hotel
	* Flight
	* Address
	* Trip
	* Visa Application
* Create service classes
	* Hotel Booking Service
	* Flight Booking Service
* Create decision logic
	* Visa check
* Create business logic
	* Public business process to deal with complete travel request
	* Private business process to deal with hotel booking
	* Private business process to deal with flight booking
* Create a test case that makes use of processes and decisions
* Configure messaging and events
* Create or import UI components using **TravelXp.com Data Index Service**
* Add metrics support for processes and decisions
* Create dashboard based on metrics


## Data model

TravelXp.com Travel Agency booking system will be based on following data model

**Traveller**

A person who requests a new travel

**Trip**

Place/Location where the traveller wants to go and dates

**Flight**

Flight that has been booked for the traveller to take him/her to the destination

**Hotel**

Place/Location where the traveller will stay during his/her travel

**Address**

Location that is associated with either traveller or hotel

**Visa Application**

Details requires to apply for visa to travel to particular country

<p align="center"><img width=75% height=75% src="docs/images/datamodel.png"></p>


## Decision logic

The decision logic will be implemented as a decision table. The logic will be responsible for verifying whether a given traveller requires a visa to enter a given country or not. The decision logic reason over the following data/facts

* Destination that the traveller wants to go - country
* Nationality of the traveller
* Length of the stay

The result will be “yes” or “no”.

<p align="centre"><img width=75% height=50% src="docs/images/decisiontable.png"></p>


## Business logic

Business logic will be based on business processes

Public process that will be responsible for orchestrating complete travel request

<p align="centre"><img width=75% height=50% src="docs/images/travels-process.png"></p>

Private process that will be responsible for booking a hotel.

<p align="centre"><img width=75% height=50% src="docs/images/book-hotel-process.png"></p>

Private process that will be responsible for booking a flight.

<p align="centre"><img width=75% height=50% src="docs/images/book-flight-process.png"></p>

##Future Improments :-

There will be services implemented to carry on the hotel and flight booking.For more details, visit
* org. acme. travels. service. Hotel Booking Service
* org.acme.travels. service. Flight Booking Service
TravelXp.com aims at improving world class amenities for all the passengers to keep them comfartable.
Soon we would make patnership with other companies and the stretch our services all over the world in feasible cost.