from flask import Flask, request
from flask_cors import CORS
from Bio.SeqUtils import molecular_weight
from Bio.Seq import Seq

# Importing Custom Errors and Error Handlers
from error_handling.custom_errors import InvalidSeqError
from error_handling.error_handlers import handle_error, handle_InvalidSeqError

app = Flask(__name__)
CORS(app)

# Registering error handlers
app.register_error_handler(InvalidSeqError, handle_InvalidSeqError)
app.register_error_handler(Exception, handle_error)



# Writing Actual Code
@app.route('/chem', methods=['POST'])
def give_result():
    try:
        formula = request.form['formula']
        exp_weight = float(request.form['weight'])
        result=[]
        w=0
        difference = 0
        
        # Convert string to a Seq object
        seq = Seq(formula)
        
        if seq:
            w = molecular_weight(Seq, "protein")
            # Calculate the molecular weight
            result.append({"Molecular_Weight": w})
            
        else: raise InvalidSeqError

        difference = w - exp_weight
        


    






    except InvalidSeqError as e:
        return handle_InvalidSeqError(e)
    
    except Exception as e:
        return handle_error(e)
    
if __name__ == '__main__':
    app.run(host='localhost', port=5500)    