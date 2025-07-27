
echo "Running Collection 1..."
python scripts/analyze_collection.py \
  --input Collection_1/challenge1b_input.json \
  --pdf-dir Collection_1/PDFs \
  --output Collection_1/challenge1b_output.json

echo "Running Collection 2..."
python scripts/analyze_collection.py \
  --input Collection_2/challenge1b_input.json \
  --pdf-dir Collection_2/PDFs \
  --output Collection_2/challenge1b_output.json

echo "Running Collection 3..."
python scripts/analyze_collection.py \
  --input Collection_3/challenge1b_input.json \
  --pdf-dir Collection_3/PDFs \
  --output Collection_3/challenge1b_output.json
