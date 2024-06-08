from transformers import TrainingArguments, default_data_collator, Trainer
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

model_name = 'distilbert-base-uncased-distilled-squad'
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model)


training_args = TrainingArguments(
    output_dir= './results',
    evaluation_strategy='epoch',
    learning_rate= 2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01 #regularization technique used to prevent overfitting by adding a penalty to the loss function based on the magnitude of the model weights.

)

data_collator = default_data_collator

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=tokenizer_dataset['train'],
#     eval_dataset=tokenizer_dataset['validation'],\
#     data_collator= data_collator,
#     tokenizer=tokenizer

# )