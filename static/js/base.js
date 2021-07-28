const DOMStrings = {
    fractionalKnapsack: 'fractional_knapsack',
    jobSequencing: 'job_sequencing',
}
const form_content = document.getElementById("form-content");

const entries = Object.entries(DOMStrings)
for (const [key, value] of entries) {
    const elementId = "#" + value;
    $(elementId).click( (e) => {
        form_content.innerHTML = fractionalKnapsackForm;
    });
}


const fractionalKnapsackForm = '<form method="get" action="" class="w-50 mx-auto fractional_knapsack_form"><div class="form-group form-row"><label for="profits" class="col-md-6">Enter Profits, separated by commas</label><div class="col-md-4"><input type="text" class="form-control form-control-sm" name="profits" id="profits" placeholder="20,40,60..."></div></div> \
<div class="form-group form-row mb-0 pb-0"><label for="weights" class="col-md-6">Enter Weights, separated by commas</label><div class="col-md-4"><input type="text" class="form-control form-control-sm" name="weights" id="weights" placeholder="10,30,50..."></div></div><div class="form-group form-row mb-0 pb-0"><label for="weights" class="col-md-6">Enter max Weight</label><div class="col-md-4"><input type="text" class="form-control" name="max_weight" id="max-weight" placeholder="Max weight"></div></div> \
<button type="submit" class="btn btn-sm btn-primary text-center solve-problem">Go</button> <div class="alert alert-primary mt-2 d-none" id="answer-response" role="alert"></div> \
</form>';