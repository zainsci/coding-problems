fn max_profit(prices: &[i32]) -> i32 {
    let mut min_price = 9999;
    let mut max_profit = 0;
    let mut i = prices.len() - 1;

    loop {
        if i == 0 {
            break;
        }

        if min_price > prices[i] {
            min_price = prices[i];
        } else if prices[i] - min_price > max_profit {
            max_profit = prices[i] - min_price;
        }
        i = i - 1;
    }

    return max_profit;
}

fn main() {
    let prices = [7, 6, 4, 3, 2, 1];
    let sol = max_profit(&prices);
    println!("{sol}");
}
