# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the \"License\");
# you may not use this file except in compliance with the License.\n",
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an \"AS IS\" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from transformers import BertForSequenceClassification
from trainer import metadata
import torch


def create(num_labels):
    """create the model by loading a pretrained model or define your
    own
    Args:
      num_labels: number of target labels
    """
    # Ensure CUDA is enabled
    print(torch.cuda.is_available())
    # Create the model, loss function, and optimizer
    model = BertForSequenceClassification.from_pretrained(
        metadata.PRETRAINED_MODEL_NAME,
        num_labels=num_labels,  # for binary classification
        output_attentions=False,
        output_hidden_states=False
    )

    return model
