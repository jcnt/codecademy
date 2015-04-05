movies = { breaking_bad: 5, 
    house_of_cars: 5,
    how_i_met_your_mother: 4,
    dr_house: 5
}

puts "What do you want to do?"
puts "add, update, display, delete"
choice = gets.chomp

case choice
when "add"
    puts "Enter your movie title"
    title = gets.chomp
    puts "What's the rating of the movie?"
    rating = gets.chomp
    if movies[title.to_sym] == nil
        movies[title.to_sym] = rating.to_i
        puts "The Movie #{title} has been added to the databse with Rating #{rating}!"
    else
        puts "This movie already exists"
    end
when "update"
    puts "Enter the title to update!"
    title = gets.chomp
    if movies[title.to_sym] == nil
        puts "Error, the movie is not in the database!"
    else
        puts "Enter the new Rating!"
        rating = gets.chomp
        movies[title.to_sym] = rating.to_i
        puts "The Movie #{title} has been updated to rating #{rating}!"
    end
when "display"
    movies.each { |title, rating| puts "#{title}: #{rating}"}
when "delete"
    puts "Enter the title to delete!"
    title = gets.chomp
    if movies[title.to_sym] == nil
        puts "Error, the movie is not in the database!"
    else
        movies.delete(title)
        puts "The movie #{title} has been deleted!"
    end
else
    puts "Error!"
end

puts
puts
puts "-----------------------------"
puts "     debug: dump database    "
puts "-----------------------------"
movies.each { |x, y| puts "#{x}: #{y}" }
