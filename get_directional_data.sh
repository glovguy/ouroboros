cat python_file_names.txt
echo "path;line" > directional_data.txt
while IFS=';' read -r path || [[ -n "$path" ]]; do
    foundstrs=$(cat $path | grep import)
    while read -r line; do
        if ! [[ $line =~ .*#.*import.* ]]; then
            echo -e "$path;$line" >> directional_data.txt
        fi
    done <<< "$foundstrs"
done < "python_file_names.txt"