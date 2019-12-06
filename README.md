# FraudDetectionAnalytics

A Simple Fraud Detection Tool for Data Analytics on a Financial Services Dataset (PaySim1).

## Introduction
The major concern of this simple research work is the analisys of the dataset through means of big data analytics and the development of a model to detect fraudulent behaviour. Every step, useful for the analysis of the data and the creation of the model, is included in this tool.

The dataset contains synthetic financial transactions based on real data and it holds five kinds of transactions: payments, cash-in, cash-out, debits and transfers. Each transaction has several fields and is tagged as fraud or genuine. For further details about the dataset, please refer to the first paper of the PaySim simulator (end of Introduction).

The research work opens with data analysis to understand the kind of data we are dealing with. Once retrieved the useful features and discovered the interesting hotspots, preprocessing is applied. The obtained dataset is then split into training and test set to build a model for fraud transactions recognition. The process of data mining is followed by the interpretation of the results.  

PaySim first paper of the simulator:
E. A. Lopez-Rojas , A. Elmir, and S. Axelsson. "PaySim: A financial mobile money simulator for fraud detection". In: The 28th European Modeling and Simulation Symposium-EMSS, Larnaca, Cyprus. 2016

## Code Organization
The code for the tool is organized in two main subfolders:

* core: contains the modules which are called by the main program and split according to each step of analysis. 
* data: contains the taxonomy of folders to store inputs, outputs and partial results. 

In the main folder it is also stored the main function to launch the tool, and the configuration file that holds the parameters about the path of the files.  

## Usage

If it is the first time running the code, set the configuration file parameters. 

Once the main menu appears, it is possible to decide which step of the analysis to begin from. 

In case you choose an intermediate step, the intermediate input is automatically loaded according to the configuration values. 

## Authors

All the following authors have equally contributed to this project (listed in alphabetical order by surname):

- Tiziano Franza ([github](https://github.com/frantiz96))

