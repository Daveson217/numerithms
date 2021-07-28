
let UIController = () =>  {
    const DOMstrings = {
        profitsTextfield: '#profits',
        weightsTextfield: '#weights',
        maxWeightTextfield: '#max-weight',
        solveBtn: '.solve-problem',
    };


    return {
        getInput: () => {            
            return {                
                profits: document.querySelector(DOMstrings.profitsTextfield).value, 
                weights: document.querySelector(DOMstrings.weightsTextfield).value, 
                maxWeight: document.querySelector(DOMstrings.maxWeightTextfield).value,
            };
        },

        getDOMstrings: () => {
            return DOMstrings;
        }, 

        clearFields: () => {

        },
    }
}

let dataController = () => {

    return {

        solveKnapsack: (profitsArray, weightsArray, maxWeight) => {
            if(profitsArray.length != weightsArray.length) {
                return -1;
            }
            ratioArrays = [];
            let map = new Map();
            for (let i = 0; i < profitsArray.length; i++) {                
                ratioArrays.push(profitsArray[i] / weightsArray[i]);                
            }

        }
    }

}

let controller = (dataCtrl, UICtrl) =>  {
    let setupEventListeners = function() {
        const DOM = UICtrl().getDOMstrings();
        
        document.querySelector(DOM.solveBtn).addEventListener('click', solveFractionalKnapsack);

        /* document.addEventListener('keypress', function(event) {
            if (event.keyCode === 13 || event.which === 13) {
                ctrlAddItem();
            }
        }); */
                    
    };

    const solveFractionalKnapsack = () => {
        
        // 1. Get the data
        input = UICtrl().getInput();
        //console.log(input);

        // 2. Split the profits
        profitsArray = input.profits.split(', ');

        // 3. Split the weights
        weightsArray = input.weights.split(', ');

        // 4. Compute the solution
        let knapsack = dataCtrl().solveKnapsack(profitsArray, weightsArray, input.maxWeight);

        // 5. Display the solution
        // check for different length of arrays
    }


    return {
        init: () => {
            console.log('Application has started.');            
            setupEventListeners();
        }
    };
}

controller(dataController, UIController).init();