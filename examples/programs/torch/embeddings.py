import torch
import torch.nn as nn


if __name__ == "__main__":
    vocab_size, dimension_size = (5, 2)
    cat_mat_embed = nn.Embedding(vocab_size, dimension_size)
    cat_tensor = torch.tensor([2])
    # creates a random embedding
    o = cat_mat_embed.forward(cat_tensor)
    print(o)
