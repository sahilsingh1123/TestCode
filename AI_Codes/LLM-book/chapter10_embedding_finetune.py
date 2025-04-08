from datasets import load_dataset
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
from sentence_transformers import losses, SentenceTransformer
from sentence_transformers.trainer import SentenceTransformerTrainer
from sentence_transformers.training_args import SentenceTransformerTrainingArguments


class EmbeddFineTune:
    def __init__(self):
        # initialise
        self._load_dataset()
        self._load_evaluator()
        self._initialise_model_and_loss_func()

    def _load_dataset(self):
        # Load MNLI dataset from GLUE
        # 0 = entailment, 1 = neutral, 2 = contradiction
        self._train_dataset = load_dataset("glue", "mnli", split="train").select(range(50_000))
        self._train_dataset = self._train_dataset.remove_columns("idx")
        self._validation_dataset_sts = load_dataset("glue", "stsb", split="validation")

    def _load_evaluator(self):
        self._evaluator = EmbeddingSimilarityEvaluator(
            sentences1=self._validation_dataset_sts["sentence1"],
            sentences2=self._validation_dataset_sts["sentence2"],
            scores=[score/5 for score in self._validation_dataset_sts["label"]],
            main_similarity="cosine"
        )

    def _initialise_model_and_loss_func(self):
        self._embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        # loss func
        self._train_loss = losses.MultipleNegativesRankingLoss(model=self._embedding_model)

        # define training arguments
        self._training_args = SentenceTransformerTrainingArguments(
            output_dir="model_dir/finetuned_embedding_model",
            num_train_epochs=1,
            per_device_train_batch_size=32,
            per_device_eval_batch_size=32,
            warmup_steps=100,
            # fp16=True,    # not supported in Apple silicone chips
            eval_steps=100,
            logging_steps=100
        )

    def train_supervised_model(self):
        self._trainer = SentenceTransformerTrainer(
            model=self._embedding_model,
            args=self._training_args,
            train_dataset=self._train_dataset,
            loss=self._train_loss,
            evaluator=self._evaluator
        )
        self._trainer.train()

    def evaluate_trained_model(self):
        self._evaluator(self._embedding_model)

ef = EmbeddFineTune()
ef.train_supervised_model()
ef.evaluate_trained_model()