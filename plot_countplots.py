import matplotlib.pyplot as plt
import seaborn as sns

def plot_countplots(df, features_col, target_col, cols_per_row=3):
    """
    Countplot для категориальных признаков с разделением по таргету
    """
    n_cols = len(features_col)
    n_rows = (n_cols + cols_per_row - 1) // cols_per_row
    
    fig, axes = plt.subplots(n_rows, cols_per_row, figsize=(cols_per_row*5, n_rows*5))
    axes = axes.flatten()
    
    for idx, col in enumerate(features_col):
        ax = axes[idx]
        
        # Строим countplot
        sns.countplot(data=df, x=col, hue=target_col, ax=ax, palette='viridis')
        
        # Добавляем проценты на столбцы
        total = len(df)
        for container in ax.containers:
            for bar in container:
                height = bar.get_height()
                if height > 0:
                    percentage = height / total * 100
                    ax.text(bar.get_x() + bar.get_width()/2., height + 5,
                           f'{percentage:.1f}%', ha='center', va='bottom', fontsize=9)
        
        ax.set_title(f'{col}', fontweight='bold', fontsize=12)
        ax.set_xlabel('')
        ax.legend(title=target_col)
        ax.grid(True)
        ax.tick_params(axis='x', rotation=45)
    
    # Скрываем пустые subplots
    for idx in range(len(features_col), len(axes)):
        axes[idx].set_visible(False)
        
    plt.suptitle(f'Распределение бинарных признаков по {target_col}\n\n', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()