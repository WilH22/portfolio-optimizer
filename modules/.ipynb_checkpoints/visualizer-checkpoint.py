def plot_portfolio_growth(portfolio_returns):
    cumulative = (1 + portfolio_returns).cumprod()

    plt.figure(figsize=(10, 5))
    plt.plot(cumulative, linewidth=2, color='green')
    plt.title("Portfolio Cumulative Return", fontsize=14, fontweight='bold')
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value (Normalized)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def plot_portfolio_weights(weights, labels):
    # 🔍 Filter out tiny or zero weights
    weights = np.array(weights)
    threshold=1e-4
    non_zero_indices = np.where(weights > threshold)[0]
    filtered_weights = weights[non_zero_indices]
    filtered_labels = [f"[{tickers[i]}]" for i in non_zero_indices]

    # 🥧 Plot
    plt.figure(figsize=(6, 6))
    patches, texts, autotexts = plt.pie(
        filtered_weights,
        labels=filtered_labels,
        autopct='%1.3f%%',
        startangle=90,
        counterclock=False
    )
    plt.title("Optimal Portfolio Allocation", fontsize=14, fontweight='bold', pad=20)

    # ✨ Style text
    for text in texts + autotexts:
        text.set_fontsize(10)

    plt.axis('equal')
    plt.tight_layout(pad=2)
    plt.show()
