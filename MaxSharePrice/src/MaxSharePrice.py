from collections import OrderedDict
from CustomExceptions import BadInputException

delim = ","
class MaxSharePriceFinder:
    """
    This class facilitates us to compute company-wise max price of shares
    along with the list of years when the price was highest
    @param csv_obj: This parameter is expected to be an open file object.
    Through this object get_max_price method iterates and processes the result.
    """
    def __init__(self, csv_obj):
        self.input_file_object = csv_obj
        #expects an open csv file object containing price data.
        #file object is iterable by default
        
        self.company_names = tuple(self.input_file_object.next().rstrip().split(",")[2:])
        #separating year, month from rest of price record
        
        self.max_price_year_wise = OrderedDict(zip(self.company_names,[None]*len(self.company_names)))
        #using OrderedDict instead of dict so that output will be in order of their presence in given csv
        #here initializing max_price_year_wise by putting Null as price for all companies
                
        self.no_of_companies = len(self.company_names)
        
        for company in  self.max_price_year_wise :
            self.max_price_year_wise[ company ]={"max_price" : 0 , "yrs_months" : []}
            #setting max_price_year_wise to the format of output
            
    def get_max_price(self):
        """
        Returns the OrderedDict object containing details of max_price of shares company wise
        along with the years & months when it attained max value.
        @param :None 
        """

        for data_line in self.input_file_object:
            line_as_list = data_line.rstrip().split(delim)
            year_month, price_data = "".join(line_as_list[:2]).rstrip(","), line_as_list[2:]
            if len(price_data) != self.no_of_companies :
                raise BadInputException

            price_data_imputed = map(eval, price_data)
            #evaluating each string value to avoid string comparison.
            #String comparison results True for "6">"555" which is not expected
            
            company_wise_price = OrderedDict(zip(self.company_names, price_data_imputed))
            
            for company in self.max_price_year_wise :
                if self.max_price_year_wise[ company ] ["max_price"] < company_wise_price[company] :        
                    self.max_price_year_wise[ company ] ["max_price"] = company_wise_price[company]
                    #If share price for a company attains max value first time
                    
                    self.max_price_year_wise[ company ] ["yrs_months"] = [year_month,]     
                    #new list is created which can hold more than one years, months for a company
                    # if share price gained max value more than once.
                                   
                elif self.max_price_year_wise[ company ] ["max_price"] == company_wise_price[company] :
                    self.max_price_year_wise[ company ] ["yrs_months"] .append( year_month)
                    #just appending year, month in appropriate list as max price is still the same
        
        return self.max_price_year_wise
        #returning the result        




if __name__ == "__main__" :
    
    csv_file_object = open("sample_data.csv")
    csv_result = MaxSharePriceFinder(csv_file_object)
    import pprint 
    pprint .pprint(csv_result.get_max_price())

