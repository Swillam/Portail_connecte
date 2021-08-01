import SwiftUI

struct ContentView: View {
    var body: some View {
        
        VStack() {
            Button(
                action: {
                // Une vibration lorsqu'on appuie sur le bouton
                    Vibration.success.vibrate()
                
                // La requete HTTP
                    URLSession.shared.dataTask(with: URL(string:"https://na7bjblg4j.execute-api.eu-west-1.amazonaws.com/default/OuvrePortailMonet?device=3")!).resume()
               }
            )
            {
                // le design du bouton (texte,gras,police, forme, arriere plan, couleur du texte)
                Text("Borne Elec Zoe")
                    .fontWeight(.bold)
                    .font(.title)
                    .padding(5)
                    .background(Color.blue)
                    .cornerRadius(40)
                    .foregroundColor(.white)
                    .padding(5)
                    .overlay(
                        RoundedRectangle(cornerRadius: 40)
                            .stroke(Color.white, lineWidth: 5)
                            )
            }
            
            
            Button(
                action: {
                    Vibration.success.vibrate()
                    URLSession.shared.dataTask(with: URL(string:"https://na7bjblg4j.execute-api.eu-west-1.amazonaws.com/default/OuvrePortailMonet?device=2")!).resume()
               }
            )
            {
                Text("Ouvrir Portillon")
                    .fontWeight(.bold)
                    .font(.title)
                    .padding(5)
                    .background(Color.blue)
                    .cornerRadius(40)
                    .foregroundColor(.white)
                    .padding(5)
                    .overlay(
                        RoundedRectangle(cornerRadius: 40)
                            .stroke(Color.white, lineWidth: 5)
                            )
            }
            
            Button(
                action: {
                    Vibration.success.vibrate()
                    URLSession.shared.dataTask(with: URL(string:"https://na7bjblg4j.execute-api.eu-west-1.amazonaws.com/default/OuvrePortailMonet?device=1")!).resume()
               }
            )
            {
                Text("Ouvrir le Portail")
                    .fontWeight(.bold)
                    .font(.title)
                    .padding(5)
                    .background(Color.blue)
                    .cornerRadius(40)
                    .foregroundColor(.white)
                    .padding(5)
                    .overlay(
                        RoundedRectangle(cornerRadius: 40)
                            .stroke(Color.white, lineWidth: 5)
                            )
            }

            
            Button(
                action: {
                    Vibration.success.vibrate()
                    URLSession.shared.dataTask(with: URL(string:"https://na7bjblg4j.execute-api.eu-west-1.amazonaws.com/default/OuvrePortailMonet?device=4")!).resume()
               }
            )
            {
                Text("Accès Cuisines")
                    .fontWeight(.bold)
                    .font(.title)
                    .padding(5)
                    .background(Color.blue)
                    .cornerRadius(40)
                    .foregroundColor(.white)
                    .padding(5)
                    .overlay(
                        RoundedRectangle(cornerRadius: 40)
                            .stroke(Color.white, lineWidth: 5)
                            )
            }
            
            
            
        }
    }
        
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .preferredColorScheme(.dark)
    }
}
